from .._api import _api, Processor

class ALLSEL(_api):
    
    processor = Processor.any

    @classmethod
    def _check(cls, command):
        raise NotImplementedError
    
    @staticmethod
    def all(entity_type: str="ALL", check: bool = True):
        '''ALLSEL 是一个便捷命令，它允许用户选择指定实体类型的所有项目，或者选择与更高层级实体的已选项目相关联的项目。这个层级结构从上到下依次为：体、面、线、关键点、单元和节点。
        当选项是ALL的时候, 会把这个结构分成两个分支。
        
        1. 体、面、线、关键点
            ALLSEL,ALL,VOLU 会选择所有体、面、线和关键点
            ALLSEL,ALL,LINE 会选择所有线和关键点
        
        2. 单元和节点
            ALLSEL,ALL,ELEM 会选择所有单元和节点
            ALLSEL,ALL,NODE 会选择所有节点
        
        ALLSEL,ALL,ALL 会选择所有项目
        '''
        if check:
            if entity_type.upper() not in ['ALL', 'VOLU', 'AREA', 'LINE', 'KP', 'ELEM', 'NODE']:
                raise ValueError("Type of the entities must be one of VOLU, AREA, LINE, KP, ELEM, NODE.")
        return f"ALLSEL,ALL,{entity_type}"

    @staticmethod
    def below(entity_type: str, check: bool = True):
        '''BELOW会根据完全的层级结构选择
        
        ALLSEL,BELOW,AREA会选择属于所选面的所有线;属于这些线的所有关键点;属于这些面、线和关键点的所有单元;以及属于这些单元的所有节点。
        
        ALLSEL,BELOW,ALL会从最高级的层级开始选择所有后续的项目。比如选择了一个体和面, 那么就会选择这个体的所有面、线、关键点、单元和节点, 忽略那个面。
        '''
        if check:
            if entity_type.upper() not in ['ALL', 'VOLU', 'AREA', 'LINE', 'KP', 'ELEM', 'NODE']:
                raise ValueError("Type of the entities must be one of VOLU, AREA, LINE, KP, ELEM, NODE.")
        return f"ALLSEL,BELOW,{entity_type}"