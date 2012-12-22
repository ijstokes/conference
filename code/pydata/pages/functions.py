from django.conf import settings


def get_file_contents(page_path):
	full_path = settings.ROOT_PATH + "/sites/" + page_path
	with open(full_path) as f:
		contents = f.read()

	return contents

def set_file_contents(page_path, contents):
	full_path = settings.ROOT_PATH + "/sites/" + page_path + "a"
	with open(full_path, 'w') as f:
		f.write(contents)
