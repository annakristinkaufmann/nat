__author__ = "Pierre-Alexandre Fonta"
__maintainer__ = "Pierre-Alexandre Fonta"

from collections import OrderedDict
from copy import deepcopy


# Raw dummy data for testing.


# DOI.
DOI = "12.3456/abcdef/ghi789"
DOI_STR = "DOI: " + DOI

# PMID.
PMID = "1234567"
PMID_STR = "PMID: " + PMID

# UNPUBLISHED ID.
UPID = "1a23b45c-67de-89f0-1234-56789g12h3i4"
UPID_STR = "UNPUBLISHED: " + UPID

# Date.
DATE = "2017-4-09"

# Creators.
CREATORS = [
    {
        "creatorType": "author",
        "firstName": "AuthorFirstA",
        "lastName": "AuthorLastA"
    },
    {
        "creatorType": "author",
        "firstName": "AuthorFirst B",
        "lastName": "AuthorLast-B"
    },
    {
        "creatorType": "author",
        "firstName": "AuthorFirst C.",
        "lastName": "AuthorLastC"
    },
    {
        "creatorType": "editor",
        "firstName": "EditorFirstA",
        "lastName": "EditorLastD"
    },
    {
        "creatorType": "editor",
        "firstName": "EditorFirst B",
        "lastName": "EditorLast-E"
    }
]


# Data returned by PyZotero. Retrieved with PyZotero 1.3.0 on 12.01.18.


# Expected item_types from Zotero.item_types().
ITEM_TYPES = [
    {"itemType": "artwork", "localized": "Artwork"},
    {"itemType": "audioRecording", "localized": "Audio Recording"},
    {"itemType": "bill", "localized": "Bill"},
    {"itemType": "blogPost", "localized": "Blog Post"},
    {"itemType": "book", "localized": "Book"},
    {"itemType": "bookSection", "localized": "Book Section"},
    {"itemType": "case", "localized": "Case"},
    {"itemType": "computerProgram", "localized": "Computer Program"},
    {"itemType": "conferencePaper", "localized": "Conference Paper"},
    {"itemType": "dictionaryEntry", "localized": "Dictionary Entry"},
    {"itemType": "document", "localized": "Document"},
    {"itemType": "email", "localized": "E-mail"},
    {"itemType": "encyclopediaArticle", "localized": "Encyclopedia Article"},
    {"itemType": "film", "localized": "Film"},
    {"itemType": "forumPost", "localized": "Forum Post"},
    {"itemType": "hearing", "localized": "Hearing"},
    {"itemType": "instantMessage", "localized": "Instant Message"},
    {"itemType": "interview", "localized": "Interview"},
    {"itemType": "journalArticle", "localized": "Journal Article"},
    {"itemType": "letter", "localized": "Letter"},
    {"itemType": "magazineArticle", "localized": "Magazine Article"},
    {"itemType": "manuscript", "localized": "Manuscript"},
    {"itemType": "map", "localized": "Map"},
    {"itemType": "newspaperArticle", "localized": "Newspaper Article"},
    {"itemType": "note", "localized": "Note"},
    {"itemType": "patent", "localized": "Patent"},
    {"itemType": "podcast", "localized": "Podcast"},
    {"itemType": "presentation", "localized": "Presentation"},
    {"itemType": "radioBroadcast", "localized": "Radio Broadcast"},
    {"itemType": "report", "localized": "Report"},
    {"itemType": "statute", "localized": "Statute"},
    {"itemType": "tvBroadcast", "localized": "TV Broadcast"},
    {"itemType": "thesis", "localized": "Thesis"},
    {"itemType": "videoRecording", "localized": "Video Recording"},
    {"itemType": "webpage", "localized": "Web Page"}
]

# [Zotero.item_template(x) for x in sorted([x["itemType"] for x in ITEM_TYPES])]
ITEM_TEMPLATES = [
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "artworkMedium": "",
        "artworkSize": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "artist", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "artwork",
        "language": "",
        "libraryCatalog": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "ISBN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "audioRecordingFormat": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "performer", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "audioRecording",
        "label": "",
        "language": "",
        "libraryCatalog": "",
        "numberOfVolumes": "",
        "place": "",
        "relations": {},
        "rights": "",
        "runningTime": "",
        "seriesTitle": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "volume": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "billNumber": "",
        "code": "",
        "codePages": "",
        "codeVolume": "",
        "collections": [],
        "creators": [{"creatorType": "sponsor", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "history": "",
        "itemType": "bill",
        "language": "",
        "legislativeBody": "",
        "relations": {},
        "rights": "",
        "section": "",
        "session": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "blogTitle": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "blogPost",
        "language": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "websiteType": ""
    },
    {
        "ISBN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "edition": "",
        "extra": "",
        "itemType": "book",
        "language": "",
        "libraryCatalog": "",
        "numPages": "",
        "numberOfVolumes": "",
        "place": "",
        "publisher": "",
        "relations": {},
        "rights": "",
        "series": "",
        "seriesNumber": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "volume": ""
    },
    {
        "ISBN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "bookTitle": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "edition": "",
        "extra": "",
        "itemType": "bookSection",
        "language": "",
        "libraryCatalog": "",
        "numberOfVolumes": "",
        "pages": "",
        "place": "",
        "publisher": "",
        "relations": {},
        "rights": "",
        "series": "",
        "seriesNumber": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "volume": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "caseName": "",
        "collections": [],
        "court": "",
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "dateDecided": "",
        "docketNumber": "",
        "extra": "",
        "firstPage": "",
        "history": "",
        "itemType": "case",
        "language": "",
        "relations": {},
        "reporter": "",
        "reporterVolume": "",
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "url": ""
    },
    {
        "ISBN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "company": "",
        "creators": [{"creatorType": "programmer", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "computerProgram",
        "libraryCatalog": "",
        "place": "",
        "programmingLanguage": "",
        "relations": {},
        "rights": "",
        "seriesTitle": "",
        "shortTitle": "",
        "system": "",
        "tags": [],
        "title": "",
        "url": "",
        "versionNumber": ""
    },
    {
        "DOI": "",
        "ISBN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "conferenceName": "",
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "conferencePaper",
        "language": "",
        "libraryCatalog": "",
        "pages": "",
        "place": "",
        "proceedingsTitle": "",
        "publisher": "",
        "relations": {},
        "rights": "",
        "series": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "volume": ""
    },
    {
        "ISBN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "dictionaryTitle": "",
        "edition": "",
        "extra": "",
        "itemType": "dictionaryEntry",
        "language": "",
        "libraryCatalog": "",
        "numberOfVolumes": "",
        "pages": "",
        "place": "",
        "publisher": "",
        "relations": {},
        "rights": "",
        "series": "",
        "seriesNumber": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "volume": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "document",
        "language": "",
        "libraryCatalog": "",
        "publisher": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "email",
        "language": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "subject": "",
        "tags": [],
        "url": ""
    },
    {
        "ISBN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "edition": "",
        "encyclopediaTitle": "",
        "extra": "",
        "itemType": "encyclopediaArticle",
        "language": "",
        "libraryCatalog": "",
        "numberOfVolumes": "",
        "pages": "",
        "place": "",
        "publisher": "",
        "relations": {},
        "rights": "",
        "series": "",
        "seriesNumber": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "volume": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "director", "firstName": "", "lastName": ""}],
        "date": "",
        "distributor": "",
        "extra": "",
        "genre": "",
        "itemType": "film",
        "language": "",
        "libraryCatalog": "",
        "relations": {},
        "rights": "",
        "runningTime": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "videoRecordingFormat": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "forumTitle": "",
        "itemType": "forumPost",
        "language": "",
        "postType": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "collections": [],
        "committee": "",
        "creators": [{"creatorType": "contributor", "firstName": "", "lastName": ""}],
        "date": "",
        "documentNumber": "",
        "extra": "",
        "history": "",
        "itemType": "hearing",
        "language": "",
        "legislativeBody": "",
        "numberOfVolumes": "",
        "pages": "",
        "place": "",
        "publisher": "",
        "relations": {},
        "rights": "",
        "session": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "instantMessage",
        "language": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "interviewee", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "interviewMedium": "",
        "itemType": "interview",
        "language": "",
        "libraryCatalog": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "DOI": "",
        "ISSN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "issue": "",
        "itemType": "journalArticle",
        "journalAbbreviation": "",
        "language": "",
        "libraryCatalog": "",
        "pages": "",
        "publicationTitle": "",
        "relations": {},
        "rights": "",
        "series": "",
        "seriesText": "",
        "seriesTitle": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "volume": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "letter",
        "language": "",
        "letterType": "",
        "libraryCatalog": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "ISSN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "issue": "",
        "itemType": "magazineArticle",
        "language": "",
        "libraryCatalog": "",
        "pages": "",
        "publicationTitle": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "volume": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "manuscript",
        "language": "",
        "libraryCatalog": "",
        "manuscriptType": "",
        "numPages": "",
        "place": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "ISBN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "cartographer", "firstName": "", "lastName": ""}],
        "date": "",
        "edition": "",
        "extra": "",
        "itemType": "map",
        "language": "",
        "libraryCatalog": "",
        "mapType": "",
        "place": "",
        "publisher": "",
        "relations": {},
        "rights": "",
        "scale": "",
        "seriesTitle": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "ISSN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "edition": "",
        "extra": "",
        "itemType": "newspaperArticle",
        "language": "",
        "libraryCatalog": "",
        "pages": "",
        "place": "",
        "publicationTitle": "",
        "relations": {},
        "rights": "",
        "section": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "collections": [],
        "itemType": "note",
        "note": "",
        "relations": {},
        "tags": []
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "applicationNumber": "",
        "assignee": "",
        "collections": [],
        "country": "",
        "creators": [{"creatorType": "inventor", "firstName": "", "lastName": ""}],
        "extra": "",
        "filingDate": "",
        "issueDate": "",
        "issuingAuthority": "",
        "itemType": "patent",
        "language": "",
        "legalStatus": "",
        "pages": "",
        "patentNumber": "",
        "place": "",
        "priorityNumbers": "",
        "references": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "audioFileType": "",
        "collections": [],
        "creators": [{"creatorType": "podcaster", "firstName": "", "lastName": ""}],
        "episodeNumber": "",
        "extra": "",
        "itemType": "podcast",
        "language": "",
        "relations": {},
        "rights": "",
        "runningTime": "",
        "seriesTitle": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "collections": [],
        "creators": [{"creatorType": "presenter", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "presentation",
        "language": "",
        "meetingName": "",
        "place": "",
        "presentationType": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "audioRecordingFormat": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "director", "firstName": "", "lastName": ""}],
        "date": "",
        "episodeNumber": "",
        "extra": "",
        "itemType": "radioBroadcast",
        "language": "",
        "libraryCatalog": "",
        "network": "",
        "place": "",
        "programTitle": "",
        "relations": {},
        "rights": "",
        "runningTime": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "institution": "",
        "itemType": "report",
        "language": "",
        "libraryCatalog": "",
        "pages": "",
        "place": "",
        "relations": {},
        "reportNumber": "",
        "reportType": "",
        "rights": "",
        "seriesTitle": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "code": "",
        "codeNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "dateEnacted": "",
        "extra": "",
        "history": "",
        "itemType": "statute",
        "language": "",
        "nameOfAct": "",
        "pages": "",
        "publicLawNumber": "",
        "relations": {},
        "rights": "",
        "section": "",
        "session": "",
        "shortTitle": "",
        "tags": [],
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "thesis",
        "language": "",
        "libraryCatalog": "",
        "numPages": "",
        "place": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "thesisType": "",
        "title": "",
        "university": "",
        "url": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "director", "firstName": "", "lastName": ""}],
        "date": "",
        "episodeNumber": "",
        "extra": "",
        "itemType": "tvBroadcast",
        "language": "",
        "libraryCatalog": "",
        "network": "",
        "place": "",
        "programTitle": "",
        "relations": {},
        "rights": "",
        "runningTime": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "videoRecordingFormat": ""
    },
    {
        "ISBN": "",
        "abstractNote": "",
        "accessDate": "",
        "archive": "",
        "archiveLocation": "",
        "callNumber": "",
        "collections": [],
        "creators": [{"creatorType": "director", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "videoRecording",
        "language": "",
        "libraryCatalog": "",
        "numberOfVolumes": "",
        "place": "",
        "relations": {},
        "rights": "",
        "runningTime": "",
        "seriesTitle": "",
        "shortTitle": "",
        "studio": "",
        "tags": [],
        "title": "",
        "url": "",
        "videoRecordingFormat": "",
        "volume": ""
    },
    {
        "abstractNote": "",
        "accessDate": "",
        "collections": [],
        "creators": [{"creatorType": "author", "firstName": "", "lastName": ""}],
        "date": "",
        "extra": "",
        "itemType": "webpage",
        "language": "",
        "relations": {},
        "rights": "",
        "shortTitle": "",
        "tags": [],
        "title": "",
        "url": "",
        "websiteTitle": "",
        "websiteType": ""
    }
]


# Constructed dummy data for testing.


# Expected reference types from get_reference_types().
REFERENCE_TYPES = sorted([x["itemType"] for x in ITEM_TYPES])

# List of expected templates from get_reference_template().
GET_REFERENCE_TEMPLATES = [OrderedDict(sorted(y.items(), key=lambda x: x[0]))
                           for y in ITEM_TEMPLATES]

# Test data for get_reference_template().
TEMPLATES_TEST_DATA = zip(REFERENCE_TYPES, ITEM_TEMPLATES, GET_REFERENCE_TEMPLATES)

# Expected reference templates from get_reference_templates().
REFERENCE_TEMPLATES = OrderedDict([(rtype, rtemplate) for rtype, rtemplate in
                                   zip(REFERENCE_TYPES, GET_REFERENCE_TEMPLATES)])

# Template of a reference of type 'journalArticle'.
ARTICLE_TEMPLATE = {
    "data": REFERENCE_TEMPLATES["journalArticle"],
    "key": "",
    "library": {},
    "links": {},
    "meta": {},
    "version": 1
}

# List of references of type 'journalArticle'.
REFERENCES = [deepcopy(ARTICLE_TEMPLATE) for x in range(7)]

# Template of a reference of type 'book'.
BOOK_TEMPLATE = {
    "data": REFERENCE_TEMPLATES["book"],
    "key": "",
    "library": {},
    "links": {},
    "meta": {},
    "version": 1
}
