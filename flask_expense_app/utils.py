import os
import pathlib


def get_app_dir(dir_name=None):
    # Extract the directory path from the script name
    app_dir = os.path.dirname(__file__)
    if dir_name:
        app_dir = os.path.join(app_dir, dir_name)
    return app_dir

def user_dir():
    exp_user_path = os.environ.get("EXPENSE_USER_PATH")
    if exp_user_path:
        path = pathlib.Path(exp_user_path)
    else:
        path = pathlib.Path(get_app_dir("io.flask.expense"))
    path.mkdir(exist_ok=True, parents=True)
    return path