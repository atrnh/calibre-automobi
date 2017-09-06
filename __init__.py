from calibre.customize import FileTypePlugin
import subprocess.check_output
import os.path

class AutoMobi(FileTypePlugin):
    """Automatically convert ebooks to .mobi on import."""

    name = 'Auto Mobi Plugin'
    description = 'Automatically convert books to .mobi on import'
    supported_platforms = ['osx']
    author = 'Ashley Trinh'
    version = (1, 0, 0)
    file_types = set(['lit', 'epub'])
    on_import = True

    def run(self, path_to_ebook):
        """Convert ebook to .mobi, return path to .mobi."""

        path_to_mobi = os.path.splitext(path_to_ebook)[0] + '.mobi'
        print subprocess.check_output(['ebook-convert', path_to_ebook, path_to_mobi])
        
        return path_to_mobi
