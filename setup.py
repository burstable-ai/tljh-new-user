from setuptools import setup

setup(
    name="tljh-new-user",
    entry_points={"tljh": ["new-user = tljh_new_user"]},
    py_modules=["tljh_new_user"],
)