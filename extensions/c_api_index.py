from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.nodes import make_refnode


class CApiIndexNode(nodes.General, nodes.Element):
    pass


class CApiIndexDirective(Directive):
    has_content = False

    option_spec = {
        "path": directives.unchanged_required,
    }

    def run(self):
        node = CApiIndexNode()
        node["path"] = self.options["path"].rstrip("/") + "/"
        return [node]


def process_api_indexes(app, doctree, fromdocname):
    env = app.env
    domain = env.get_domain("c")

    for node in list(doctree.findall(CApiIndexNode)):
        path = node["path"]

        categories = {
            "type": ("Data Types", []),
            "macro": ("Macros", []),
            "function": ("Functions", []),
        }

        for name, dispname, objtype, docname, anchor, priority in domain.get_objects():
            if objtype not in categories:
                continue

            if not docname.startswith(path):
                continue

            categories[objtype][1].append(
                (dispname, docname, anchor)
            )

        content = []

        for objtype in ("type", "macro", "function"):
            title, objects = categories[objtype]

            if not objects:
                continue

            section = nodes.section(ids=[f"api-index-{objtype}"])
            section += nodes.title(text=title)

            bullet_list = nodes.bullet_list()

            for dispname, docname, anchor in sorted(
                objects,
                key=lambda obj: obj[0].lower(),
            ):
                item = nodes.list_item()
                paragraph = nodes.paragraph()

                reference = make_refnode(
                    app.builder,
                    fromdocname,
                    docname,
                    anchor,
                    nodes.literal(text=dispname),
                    dispname,
                )

                paragraph += reference
                item += paragraph
                bullet_list += item

            section += bullet_list
            content.append(section)

        node.replace_self(content)


def setup(app):
    app.add_node(CApiIndexNode)

    app.add_directive(
        "c-api-index",
        CApiIndexDirective,
    )

    app.connect(
        "doctree-resolved",
        process_api_indexes,
    )

    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
