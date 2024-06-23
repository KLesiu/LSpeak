import { ModulesEnum } from "../enums/ModulesEnum"
import { Level } from "./LevelsInterfaces"

export interface CurrentLearnSession extends Level{
    texts:Question[]
    moduleId:ModulesEnum
    moduleName:string,
}

export interface Question{
    pl:string,
    eng:string,
    ger:string
}

