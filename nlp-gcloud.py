from google.cloud import language_v1

gcs_content_uri = "gs://kt38/full-output.txt"

client = language_v1.LanguageServiceClient()

type_ = language_v1.Document.Type.PLAIN_TEXT

language = "en"
document = {"gcs_content_uri": gcs_content_uri, "type_": type_, "language": language}

encoding_type = language_v1.EncodingType.UTF8

response = client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})


with open('full-entities.txt', 'w') as f:
    print(response, file=f)

with open('entities.txt', 'w') as f:
    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name), file=f)
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name), file=f)
        # Get the salience score associated with the entity in the [0, 1.0] range
        print(u"Salience score: {}".format(entity.salience), file=f)
        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{}: {}".format(metadata_name, metadata_value), file=f)

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content), file=f)
            # Get the mention type, e.g. PROPER for proper noun
            print(
                u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name), file=f
            )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language), file=f)

