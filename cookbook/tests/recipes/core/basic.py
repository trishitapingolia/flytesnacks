from cookbook.recipes.core.basic import basic_workflow, folders, files
import os


def test_basic_wf():
    res = basic_workflow.my_wf(a=3, b="hello")
    assert res == (5, "helloworld")


def test_folders():
    output_dir = folders.download_and_rotate()
    files = os.listdir(output_dir)
    assert len(files) == 2


def test_files():
    output_file = files.rotate_one_workflow(in_image=files.default_images[0])
    assert os.path.exists(output_file)