from aws_pdk.monorepo import MonorepoPythonProject

project = MonorepoPythonProject(
    dev_deps=["@aws/pdk"],
    module_name="my_project",
    name="my-project",
)

project.synth()