
from tkinter import filedialog as _Dialog

class EntityWorldClass:
    
    entityId = 0
    entityScript = ''
    
    bEntitySpawned = bool
    
    def getEntity(entity):
        entity = EntityWorldClass()
        return entity
    
    def getEntityId(entity)->int:
        entity = EntityWorldClass()
        return entity.entityId
    
    def getEntityScription(entity)->str:
        entity = EntityWorldClass()
        return entity.entityScript
    
    def EntityIsSpawned(entity)->bool:
        entity = EntityWorldClass()
        if entity.getEntityId(entity) == 0:
            return entity.bEntitySpawned == False
        if entity.getEntityId(entity) == 1:
            return entity.bEntitySpawned == True
        
    def EntityOpenMdlFile():
        entity = EntityWorldClass()
        _file = '' or __file__
        entity_filetypes = [("*.espmdl", "*.espmdl"), ("*.espentity", "*.espentity")]
        _entitytitle = 'Open Entity File'
        
        entityDialog = _Dialog.askopenfilename(defaultextension= _file, filetypes= entity_filetypes, title= _entitytitle)
        entityDialog.show()
        
        #buffering the model file format
        sBuff = [2048]
        
        if entityDialog:
            open(file= _file, mode= 'b', buffering= sBuff or -1)
        
        ##for i in range( 0 >> 1):