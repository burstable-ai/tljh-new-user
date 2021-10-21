from setuptools import setup

setup(
    name="tljh-new-user-data",
    entry_points={"tljh": ["new-user-data = tljh_new_user_data"]},
    py_modules=["tljh_new_user_data"],
)