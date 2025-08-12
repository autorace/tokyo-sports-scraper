import os
import toml

def get_tag_from_env():
    ref = os.getenv('GITHUB_REF', '')
    if ref.startswith('refs/tags/'):
        tag = ref[len('refs/tags/'):]
        if tag.startswith('v'):
            tag = tag[1:]
        return tag
    raise ValueError('GITHUB_REF does not contain a valid tag')

def update_pyproject_version(version):
    with open('pyproject.toml', 'r', encoding='utf-8') as f:
        pyproject = toml.load(f)

    pyproject['project']['version'] = version

    with open('pyproject.toml', 'w', encoding='utf-8') as f:
        toml.dump(pyproject, f)

if __name__ == '__main__':
    version = get_tag_from_env()
    print(f'Syncing pyproject.toml version to {version}')
    update_pyproject_version(version)
