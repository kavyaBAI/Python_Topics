import dbApi
import data_encryption
import os
import re
import ruamel.yaml
from ruamel.yaml.scalarstring import DoubleQuotedScalarString

def write_yaml(credentials):
    for i in credentials:
        val = i[0][0]
        val1 = val.lower().replace(' ', '_').replace('-', '_')
        #print(val1)
        yaml_filepath = f'/home/kavyabai/all_dir/{val1}.yaml'
        os.makedirs(os.path.dirname(yaml_filepath), exist_ok=True)
        with open(yaml_filepath, 'w') as file:
            content = {
                'app_name': f"cloud_optimal_{val1}",
                'python_dir': '.',
                'env_name': 'icco',
                'jars': ["target/azurecost-jar-with-dependencies.jar".replace('"',' ')],
                'tasks': []
            }
            for idx, data in enumerate(i):
                cust_name, azure_subscription, azure_client_id, azure_tenant_id, azure_client_secret, partner_tenant_id, billing_id = data
                if billing_id:
                    task_name = f"{cust_name.lower().replace(' ', '_')}"
                    task = {
                        'task_name': f"azurecost_{task_name}_{idx}",
                        'type': 'Task',
                        'config': {
                            'taskClass': 'ext.grainite.tasks.azure.costmanagement.CostDetailsReportsTask',
                            'taskInstanceClass': 'ext.grainite.tasks.azure.costmanagement.CostDetailsReportsInstance',
                            'subscriptionId': f"$secret:{task_name}_{idx}_azure_tenant_id_azure_subscription",
                            'taskName': f"azurecost_{task_name}_{idx}",
                            'tenantId': f"$secret:{task_name}_{idx}__azure_tenant_id",
                            'clientId': f"$secret:{task_name}_{idx}_azure_client_id",
                            'clientSecret': f"$secret:{task_name}_{idx}_azure_client_secret",
                            'partnerTenantId': f"$secret:{task_name}_{idx}_azure_partner_tenant_id",
                            'billingId': f"$secret:{task_name}_{idx}__azure_billing_id",
                            'delaySeconds': 14400,
                            'keyFields': 'SubscriptionId,resourceGroupName',
                            'output.table': 'cloud_optimal:resource_group_table',
                            'output.table_action': 'handle_event',
                                        'debug': True,
                            'deltasOnly': False
                        }
                    }
                    content['tasks'].append(task)

                    task = {
                        'task_name': f"desktopscan_{task_name}_{idx}",
                        'type': 'Task',
                        'config': {
                            'taskClass': 'ext.grainite.tasks.azure.desktopvirtualization.DesktopVirtualizationTask',
                            'taskInstanceClass': 'ext.grainite.tasks.azure.desktopvirtualization.DesktopVirtualizationInstance',
                            'subscriptionId': f"$secret:{task_name}_{idx}_ds_subscription",
                            'tenantId': f"$secret:{task_name}_{idx}__ds_tenant_id",
                            'clientId': f"$secret:{task_name}_{idx}_ds_client_id",
                            'clientSecret': f"$secret:{task_name}_{idx}_ds_client_secret",
                            'delaySeconds': 300,
                            'keyFields': 'SubscriptionId,resourceGroupName',
                            'deltasOnly': False,
                            'output.table': 'cloud_optimal:resource_group_table',
                            'output.table_action': 'handle_desktop_event',
                            'debug': True
                        }
                    }
                    content['tasks'].append(task)

            yaml = ruamel.yaml.YAML()
            yaml.indent(mapping=2, sequence=4, offset=2)
            yaml.dump(content, file)

    print("YAML files created successfully.")


def update_sh_file(credentials):
    for i in credentials:
        val = i[0][0]
        val1 = val.lower().replace(' ', '_').replace('-', '_')
        print(val1)
        sh_filepath = f'/home/kavyabai/all_dir/{val1}_anunta.sh'
        os.makedirs(os.path.dirname(sh_filepath), exist_ok=True)
        with open(sh_filepath, 'w') as file:
            content = ''  # Initialize content as an empty string
            for idx, data in enumerate(i):
                cust_name, azure_subscription, azure_client_id, azure_tenant_id, azure_client_secret,partner_tenant_id,billing_id = data
                # Check if the dataset already exists in the file
                pattern = fr'{cust_name.lower().replace(" ", "_")}_{idx}\s+'  # e.g., 'Anunta_Dev_0 '
                if re.search(pattern, content):
                    continue
                if billing_id:

                 # Generate the command to add/update the dataset
                    command = f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_subscription {azure_subscription} -c {cust_name.lower().replace(' ', '_')}_app.yaml\n"
                    command += f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_tenant_id {azure_tenant_id} -c {cust_name.lower().replace(' ', '_')}_app.yaml\n"
                    command += f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_client_secret {azure_client_secret} -c {cust_name.lower().replace(' ', '_')}_app.yaml\n"
                    command += f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_client_id {azure_client_id} -c {cust_name.lower().replace(' ', '_')}_app.yaml\n"
                    command += f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_partner_tenant_id {partner_tenant_id} -c {cust_name.lower().replace(' ', '_')}_app.yaml\n"
                    command += f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_billing_id {billing_id} -c {cust_name.lower().replace(' ','_')}_app.yaml\n"
                    command += f"\n"
                else:
                    command = f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_subscription {azure_subscription} -c {cust_name.lower().replace(' ', '_')}_app.yaml\n"
                    command += f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_tenant_id {azure_tenant_id} -c {cust_name.lower().replace(' ', '_')}_app.yaml\n"
                    command += f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_client_secret {azure_client_secret} -c {cust_name.lower().replace(' ', '_')}_app.yaml\n"
                    command += f"gx secret put {cust_name.lower().replace(' ', '_')}_{idx}_azure_client_id {azure_client_id} -c {cust_name.lower().replace(' ', '_')}_app.yaml\n"
                    command += f"\n"


                # Replace the existing dataset if found
                pattern = fr'gx secret put {cust_name.lower().replace(" ", "_")}_{idx}[^a-zA-Z0-9]'
                content = re.sub(pattern, command, content)
                # Append the dataset if not found
                if pattern not in content:
                    content += command
                    file.write(content)
    print("script.sh file created successfully.")
def decrypt_data(sub_idxs):
    #print(sub_idxs)
    updated_sub_idxs = []
    for tup in sub_idxs:
        client_name =  tup[0]
        #print(tup)
        appid = tup[2]
        d_appid = data_encryption.decrypt(client_name,appid)
        #print( d_appid)
        tenant_id = tup[3]
        d_tenant_id = data_encryption.decrypt(client_name,tenant_id)
        #print( d_tenant_id)
        ptenant_id = tup[5]
        d_ptenant_id = data_encryption.decrypt(client_name,ptenant_id)
        #print( d_ptenant_id)
        secret_key = tup[4]
        d_secret_key = data_encryption.decrypt(client_name,secret_key)
        #print( d_secret_key)
        updated_tup = (tup[0],tup[1], d_appid,d_tenant_id,d_secret_key,d_ptenant_id,tup[6])
        updated_sub_idxs.append(updated_tup)
       # print(updated_sub_idxs
    return updated_sub_idxs


def main(file_path,dbstring):
    #file_path = 'app_cp.yaml'
    #dbstring = "20.12.46.172#ai-user1#User@123#cq_icco_master"
    #c_names =  read_cust_in(dbstring)
    cred_list = []
    #for company_name in c_names:
    c_names = dbApi.read_cust_in(dbstring)
    c_name = ['National Grid']
    #c_name = ['Titan_Dev/QA/Demo','SW_WDV/TESTING','FPC _Production_Control plane','DR_Production_Control plane',]
    #c_name = ['DR_Zenworx','DR_SAXLLP','DR_MPA MEDIA','Managing Patners','InfoSync']
    #c_name = ['HGS CSE Citrix','ABSLi','ABSLI - AVD','HGS CES','IIFL','Firstsource Solutions Ltd','Mumbai Ops','BCP_DaaS','DR_MaximSoftware','DR_Auctusgroup','Titan_Production_Control plane','DR_TowerMSA','DR_TranTax']
    for company_name in c_names:
        if company_name not in c_name:continue
        all_cred =  dbApi.get_credentials(dbstring, company_name)
        cred = decrypt_data(all_cred)
        cred_list.append(cred)
        cred_list.append(cred)
    #print(cred_list)
    update_sh_file(cred_list)
    #write_yaml(cred_list)


if __name__ == "__main__":
    file_path = 'app_cp.yaml'
    #sh_file = '/home/azureuser/cloud_optimal/secrets-anunta.sh'
    dbstring = "20.12.46.172#ai-user1#User@123#cq_icco_master_new"
    main(file_path,dbstring)

                        