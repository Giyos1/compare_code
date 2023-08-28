# import ast
#
#
# def compare_ast_trees(tree1, tree2):
#     return ast.dump(tree1) == ast.dump(tree2)
#
#
# def check_plagiarism(text1, text2, threshold=0.7):
#     tree1 = ast.parse(text1)
#     tree2 = ast.parse(text2)
#
#     if compare_ast_trees(tree1, tree2):
#         similarity = len(text2) / len(text1)
#         if similarity >= threshold:
#             return True, similarity
#     return False, 0
#
#
# # Example usage
# if __name__ == "__main__":
#     code1 = """
#     def calculate_square(x):
#         return x * x
#     """
#
#     code2 = """
#     def calculate_square(y):
#         return y * y
#     """
#
#     is_plagiarized, similarity = check_plagiarism(code1, code2)
#
#     if is_plagiarized:
#         print("Plagiarism detected! Similarity:", similarity)
#     else:
#         print("No plagiarism detected. Similarity:", similarity)
