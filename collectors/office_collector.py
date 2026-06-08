from docx import Document

def get_docx_metadata(file_path):

    doc = Document(file_path)

    props = doc.core_properties

    return {
        "Author": props.author, 

        "Category": props.category,

        "Comments": props.comments,

        "ContentStatus":
            props.content_status,

        "Created":
            props.created,

        "Identifier":
            props.identifier,

        "Keywords":
            props.keywords,

        "Language":
            props.language,

        "LastModifiedBy":
            props.last_modified_by,

        "Revision":
            props.revision,

        "Subject":
            props.subject,

        "Title":
            props.title,

        "Version":
            props.version
    }