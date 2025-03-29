import pathlib

BASE_DIR = pathlib.Path(__file__).parent
DOCS_DIR = BASE_DIR / 'docs'

def on_config(config, **kwargs):
    "Add the functions variables and filters to the mix"
    i18n_plugin = config.plugins.get('i18n')
    macros_plugin = config.plugins.get("macros")
    langs = i18n_plugin.all_languages
    filUnitBOMs = {}
    for lang in langs:
        filename = 'filUnitBOM.md' if lang == 'en' else f'filUnitBOM.{lang}.md'
        try:
            with open(DOCS_DIR / filename) as file:
                filUnitBOMs[lang] = file.read()
        except FileNotFoundError as e:
            if lang == 'en':
                raise e
            else:
                filUnitBOMs[lang] = filUnitBOMs['en']

        varName = 'filUnitBOM' if lang == 'en' else f'filUnitBOM{lang}'
        macros_plugin.register_variables({varName: filUnitBOMs[lang]}) 