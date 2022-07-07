
from typing import Optional

from binarytree import Node, bst, tree


def random_tree(
    height: int = 4,
    is_perfect: bool = False,
    letters: bool = False,
) -> Optional[Node]:
    """随机生成一棵树."""
    return tree(height, is_perfect, letters)


def random_bst(
    height: int = 4,
    letters: bool = False,
):
    """随机生成一棵二叉搜索树."""
    return bst(height, False, letters)


if __name__ == "__main__":
    root = random_bst()
    print(root)
