def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage:
products = ["apple", "banana", "orange", "apple", "grape"]
target_product = "apple"
result = linear_search_product(products, target_product)
print("Indices of", target_product, ":", result)
