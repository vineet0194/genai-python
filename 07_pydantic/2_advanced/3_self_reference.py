from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None       # refers to self (forward references)

# This is called a forward reference, since python doesnt know that Comment exists 'yet'.
# we forward reference Comment class by typing it in strings instead of passing the class entirely

# ! REBUILDING :

# After the class is completely created,

# class Comment(...):               # now the name Comment finally exists.
#     ...

# But Pydantic still remembers 'Comment' as just a string.

# Calling Comment.model_rebuild()

# tells Pydantic: "Go back through all the annotations, find any forward references (strings),
# and replace them with the actual Python classes."

# So internally,

# Before rebuilding:

# replies
#     ↓
# List["Comment"]   # just text

# After rebuilding:

# replies
#     ↓
# List[Comment]     # actual class object

# Now Pydantic knows that every reply should itself be validated as a Comment.
Comment.model_rebuild

# In Pydantic v2, many forward references are resolved automatically.
# Automatic resolution doesn't always work. It can fail when thereferenced
# type isn't available yet or when models depend on each other.

comment = Comment(
    id= 1,
    content = "First comment",
    replies = [
        Comment(id=2, content="Reply 1"),
        Comment(id=3, content="Reply 2", replies = [
            Comment(id=4, content="Reply to Reply 2")
        ])
    ]
)