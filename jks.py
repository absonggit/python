import jenkins
server = jenkins.Jenkins('http://2.2.2.4',username='admin',password='123456')
# version = server.get_version()
# print(version)
#print(server.get_all_jobs())

# build_parameters = {
#     'parameters': [
#         {'_class': 'hudson.scm.listtagsparameter.ListSubversionTagsParameterValue','name': 'BRANCH', 'tag': 'dev', 'tagsDir': 'svn://2.2.2.6/myproject'},
#         {'_class': 'hudson.model.StringParameterValue', 'name': 'REVISION', 'value': 'HEAD'},
#         {'_class': 'hudson.model.StringParameterValue', 'name': 'HOST_GROUP', 'value': 'dev_web'},
#         {'_class': 'com.cwctravel.hudson.plugins.extended_choice_parameter.ExtendedChoiceParameterValue', 'name': 'PRODUCT', 'value': 'all'},
#         ]
#         }
# server.build_job("jenkins_svn",parameters=build_parameters)
#print(server.get_build_info("jenkins_svn", 207))
#print(server.get_build_console_output("jenkins_svn", 203))
print(server.get_build_info('jenkins_svn', 207))