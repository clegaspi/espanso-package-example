import re

from espanso import Espanso

test_links = {
'org_projects_link': 'https://cloud.mongodb.com/v2#/org/5c78495d9ccf64c3f731f625/projects',
'org_settings_link': 'https://cloud.mongodb.com/v2#/org/5c78495d9ccf64c3f731f625/settings/general',
'project_dep_dbs_link': 'https://cloud.mongodb.com/v2/5ef573a1be117b63de26cecf#clusters',
'project_dep_triggers_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#triggers',
'project_dep_datalakes_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#dataLakes',
'project_sec_db_access_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#security/database/users',
'project_sec_network_access_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#security/network/accessList',
'project_sec_advanced_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#security/advanced',
'project_int_processes_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#deployment/list',
'cluster_overview_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#clusters/detail/toxmaxbot',
'cluster_metrics_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#host/replicaSet/610c8ba0e8b9570357d187d8',
'cluster_realtime_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#metrics/replicaSet/610c8ba0e8b9570357d187d8/realtime/panel',
'cluster_data_explorer_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#metrics/replicaSet/610c8ba0e8b9570357d187d8/explorer/some_db/some_coll/find',
'cluster_atlas_search_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#clusters/atlasSearch/toxmaxbot',
'cluster_profiler_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#metrics/replicaSet/610c8ba0e8b9570357d187d8/profiler',
'cluster_pa_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#metrics/replicaSet/610c8ba0e8b9570357d187d8/profiler',
'cluster_online_archive_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#clusters/onlineArchive/toxmaxbot',
'cluster_command_line_tools_link': 'https://cloud.mongodb.com/v2/5c78495d9ccf64c3f731f628#clusters/commandLineTools/toxmaxbot',
'bogus_link': 'https://something.notreal'
}


def make_atlas_link_text(raw_value):
    link = Espanso.replace(raw_value)
    # perform the initial regex match
    link_components = re.match(
        r'https:\/\/cloud\.mongodb\.com\/(?P<is_atlas>v2)(?P<is_org>(?:#\/org)?)\/(?P<id>[a-f0-9]{24})(?:#|\/)(?P<tail>.*)', 
        link
    )

    # determine if the link points to some Atlas resource. Else, return the original value provided
    if not link_components:
        return f'Relevant Link|{link}'

    # interpret the tail end to gather identifying details
    trailing_link_components = re.match(
        r'(?:.+\/(?P<cluster_id>[a-f0-9]{24})\/?|clusters.+\/(?P<cluster_name>.+$))',
        link_components['tail']
    )
    
    # determine if the link points to something at the org level or the project level
    if link_components['is_org']:
        return f'Org Link|[{link_components["id"]}]({link}) - *{Espanso.get("capture.instance_size")}*'
    if link_components['is_atlas']:
        if link_components['tail'].startswith('clusters'):
            if not trailing_link_components:
                # we know this is a project link
                return f'Project Link|[{link_components["id"]}]({link}) - *{Espanso.get("capture.instance_size")}*'
            return f'Cluster Link|[{trailing_link_components["cluster_name"]}]({link}) - *{Espanso.get("capture.instance_size")}*'
        elif link_components['tail'].startswith('host') or link_components['tail'].startswith('metrics'):
            # we know this is a cluster link
            return f'Cluster Link|[{trailing_link_components["cluster_id"]}]({link}) - *{Espanso.get("capture.instance_size")}*'
        else:
            # we know this is a project link
            return f'Project Link|[{link_components["id"]}]({link}) - *{Espanso.get("capture.instance_size")}*'

if __name__ == '__main__':
        Espanso.run(make_atlas_link_text)
    