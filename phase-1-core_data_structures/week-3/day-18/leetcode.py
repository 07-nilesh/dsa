class ProductOfNumbers:

    def __init__(self):
        
        self.prefix_product=[1]

    def add(self, num: int) -> None:
        if num ==0:
            self.prefix_product.clear()
            self.prefix_product=[1]
        else:

            nos=num*self.prefix_product[-1]
            self.prefix_product.append(nos)
        
        

    def getProduct(self, k: int) -> int:
        if len(self.prefix_product)<=k:
            return 0
        return self.prefix_product[-1]//self.prefix_product[len(self.prefix_product)-1-k]

        



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)