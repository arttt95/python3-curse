from importlib import metadata

# print(metadata.version('pip'))

# metadados_pip = metadata.metadata('pip')
#
# print(list(metadados_pip))
#
# print(metadados_pip['Summary'])

# print(len(metadata.files('pip')))

# print(metadata.requires('pip'))

print(metadata.requires('django'))
