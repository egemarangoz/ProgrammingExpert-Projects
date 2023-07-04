"""
Assessment 3.5 - FileSystem Implementation

In this question, you need to implement a very simplistic "FileSystem" class that mimics the way that your
own computer's FileSystem works. A FileSystem starts empty with only a root node which will
always be a directory.

A FileSystem is a tree-like structure composed of nodes, each of which is either a File or Directory.

Files are simplest and only have names and contents as attributes; which correspond to the name of
the file and its contents, respectively. Files also have a write method, which sets the contents of that file
to the argument passed in. Additionally, files override the __len__ dunder method which returns the
number of characters in the contents of that file.

Directories have a name and a children attribute. children is a dictionary that stores the name of
its children nodes as keys, and the nodes themselves as the values of that dictionary. Directories also have
the add and delete methods which are used to add or delete nodes from its children dictionary.

For your convnience, the __str__ methods of each class have been overridden so tha tyou may debug
your FileSystem more easily.

Your task is to implement the following methods on the FileSystem class:

- create_directory(path): This method should create a Directory inside the FileSystem
at the location specified. For instance, create_dictionary("/dir1") should create a directory as
a child of the root of the filesystem called "dir1". Running
createdictionary("/dir1/dir2") should create another directory, dir2, inside the one that
was just created. If the path is malformed or the operation is impossible, it should raise a
ValueError.

- create_file(path, contents): This method should create a new file at the desired path, with
the contents passed in. If the operation is impossible, it should raise a ValueError.

- read_file(path): This method should return th contents of the file at the path parameter. If no
such file exists, it should raise a ValueError.

- delete_directory_or_file(path): This method should delete the node located at path. It should 
work on files and directories alike, and should raise a ValueError if that file does not exist.

- size(): This methods should return the number o characters across all files in your filesystem.

- _find_bottom_node(node_names): This is a private helper method of the FileSystem class that takes in 
a list of node names and should traverse the filesystem downwards until the last node in the list. 
For instance, calling this with ["a", "b", "c"] should first look for a node a inside the root node of the 
filesystem, then for a node b inside node a, and then return the node c which should be a child of node b.

Note: For all methods that accept a path parameter you will need to first validate that path and then parse it.
The path will be a string, and from that string you'll need to do one of the following:
- Obtain the directory object used to create a new directory or file inside of.
- Obtain the directory object used to delete a directory or file.
- Obtain the file object to read the contents of.

This is non-trivial because you may need to distinguish between the name of the new node created
and the path where this node should not be created

"""

class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def create_directory(self, path):
        FileSystem._validate_path(path)

        path_node_names = path[1:].split("/")
        middle_node_names = path_node_names[:-1]
        new_directory_name = path_node_names[-1]

        before_last_node = self._find_bottom_node(middle_node_names)
        
        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} isn't a directory.")
        
        new_directory = Directory(new_directory_name)

        before_last_node.add_node(new_directory)

    def create_file(self, path, contents):
        FileSystem._validate_path(path)

        path_node_names = path[1:].split("/")
        middle_node_names = path_node_names[:-1]
        new_file_name = path_node_names[-1]

        before_last_node = self._find_bottom_node(middle_node_names)
        
        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} isn't a directory.")
        
        new_file = File(new_file_name)
        new_file.write_contents(contents)

        before_last_node.add_node(new_file)

    def read_file(self, path):
        FileSystem._validate_path(path)

        path_node_names = path[1:].split("/")
        middle_node_names = path_node_names[:-1]
        file_name = path_node_names[-1]

        before_last_node = self._find_bottom_node(middle_node_names)
        
        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} isn't a directory.")

        if file_name not in before_last_node.children:
            raise ValueError(f"File not found: {file_name}.")
            
        return before_last_node.children[file_name].contents

    def delete_directory_or_file(self, path):
        FileSystem._validate_path(path)

        path_node_names = path[1:].split("/")
        middle_node_names = path_node_names[:-1]
        node_to_delete_name = path_node_names[-1]

        before_last_node = self._find_bottom_node(middle_node_names)
        
        if not isinstance(before_last_node, Directory):
            raise ValueError(f"{before_last_node.name} isn't a directory.")

        if node_to_delete_name not in before_last_node.children:
            raise ValueError(f"Node not found: {node_to_delete_name}.")
            
        before_last_node.delete_node(node_to_delete_name)

    def size(self):
        size = 0
        nodes = [self.root]
        while len(nodes) > 0:
            current_node = nodes.pop()
            if isinstance(current_node, Directory):
                children = list(current_node.children.values())
                nodes.extend(children)
                continue

            if isinstance(current_node, File):
                size += len(current_node)

        return size

    def __str__(self):
        return f"*** FileSystem ***\n" + self.root.__str__() + "\n***"
    
    @staticmethod
    def _validate_path(path):
        if not path.startswith("/"):
            raise ValueError("Path should start with `/`.")


    def _find_bottom_node(self, node_names):
        current_node = self.root
        for node_name in node_names:
            if not isinstance(current_node, Directory):
                raise ValueError(f"{current_node.name} isn't a directory.")

            if node_name not in current_node.children:
                raise ValueError(f"Node not found: {node_name}.")

            current_node = current_node.children[node_name]
            
        return current_node


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({type(self).__name__})"


class Directory(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_node(self, node):
        self.children[node.name] = node

    def delete_node(self, name):
        del self.children[name]

    def __str__(self):
        string = super().__str__()

        children_strings = []
        for child in list(self.children.values()):
            child_string = child.__str__().rstrip()
            children_strings.append(child_string)

        children_combined_string = indent("\n".join(children_strings), 2)
        string += "\n" + children_combined_string.rstrip()
        return string


class File(Node):
    def __init__(self, name):
        super().__init__(name)
        self.contents = ""

    def write_contents(self, contents):
        self.contents = contents

    def __len__(self):
        return len(self.contents)

    def __str__(self):
        return super().__str__() + f" | {len(self)} characters"


def indent(string, number_of_spaces):
    spaces = " " * number_of_spaces
    lines = string.split("\n")
    indented_lines = [spaces + line for line in lines]
    return "\n".join(indented_lines)
