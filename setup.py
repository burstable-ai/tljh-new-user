from setuptools import setup

setup(
    name="tljh-new-user-data",
    entry_points={"tljh": ["new-user-data = cb_new_user"]},
    py_modules=["cb_new_user"],
)