from mutagen import File

def get_audio_metadata(file_path):

    audio = File(file_path)

    metadata = {}

    if audio:
        metadata["Length"] = getattr(
            audio.info,
            "length",
            None
        )

        metadata["Bitrate"] = getattr(
            audio.info,
            "bitrate",
            None
        )

        if audio.tags:

            for key, value in audio.tags.items():

                metadata[key] = str(value)

    return metadata
    