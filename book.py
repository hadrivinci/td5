class Book:
    def __init__(self, name):
        self.name = name
        # dict format: {key: {id: volume, id: volume, id: volume}}
        self.sellDict = {}
        self.buyDict = {}
        self.lastId = 0

    def display_book(self, volume, price, buy):
        sOuput = 'Book on ' + self.name
        print(sOuput)
        for price in sorted(self.sellDict):
            priceDict = self.sellDict[price]
            for nId in priceDict:
                sOuput = '        SELL ' + repr(priceDict[nId]) + '@' + repr(price) + ' id=' + repr(nId) + ' on ' + self.name
                print(sOuput)
        for price in sorted(self.buyDict, key=None, reverse=True):
            priceDict = self.buyDict[price]
            for nId in priceDict:
                sOuput = '        BUY ' + repr(priceDict[nId]) + '@' + repr(price) + ' id=' + repr(nId) + ' on ' + self.name
                print(sOuput)
        print('-----------------------------')
        return
            
        
    def insert_book(self, volume, price, buy):
        # Display Insert inform text
        if buy:
            sOuput = '---Insert BUY'
        else:
            sOuput = '---Insert SELL'
        sOuput = sOuput + repr(volume) + '@' + repr(price) + ' on ' + self.name
        print(sOuput)

        # inDict is the dict that can be increased (add new order)
        # deDict is the dict that can be decreased (reduce amount)
        if buy:
            inDict = self.buyDict
            deDict = self.sellDict
        else:
            inDict = self.sellDict
            deDict = self.buyDict
        
        #execute if any
        deList = sorted(deDict, key=None, reverse=not buy)
        finalVol = volume
        for key in deList:
            # we use the price as the key to store order
            # if lowest sell price is higher than buy price, break
            if buy:
                if key > price:
                    break
            else: #sell
            # if lowest buy price is higher than sell price, break
                if key < price:
                    break
            priceDict = deDict[key]
            orderIdList = sorted(priceDict)
            for nId in orderIdList:
                if finalVol < priceDict[nId]:
                    sOuput = 'Executed ' +  repr(finalVol) + ' at ' + repr(key) + ' on ' + self.name
                    priceDict[nId] = priceDict[nId] - finalVol
                    finalVol = 0
                    deDict[key] = priceDict
                    print(sOuput)
                    break
                elif finalVol == priceDict[nId]:
                    sOuput = 'Executed ' +  repr(finalVol) + ' at ' + repr(key) + ' on ' + self.name
                    del priceDict[nId]
                    if not priceDict:
                        del deDict[key]
                    else:
                        deDict[key] = priceDict
                    finalVol = 0
                    print(sOuput)
                    break
                else: # finalVol > priceDict
                    sOuput = 'Executed ' +  repr(priceDict[nId]) + ' at ' + repr(key) + ' on ' + self.name
                    finalVol = finalVol - priceDict[nId]
                    del priceDict[nId]
                    print(sOuput)
            if finalVol <= 0:
                break
        if finalVol > 0:
            self.lastId = self.lastId + 1
            if price in inDict:
                inDict[price][self.lastId] = finalVol
            else:
                newPrice = {self.lastId: finalVol}
                inDict[price] = newPrice
                inDict[price][self.lastId] = finalVol

        self.display_book(volume, price, buy)
        return
    
    def insert_buy(self, volume, price):
        self.insert_book(volume, price, True)
        return

    def insert_sell(self, volume, price):
        self.insert_book(volume, price, False)
        return
