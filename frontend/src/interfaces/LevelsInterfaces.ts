import { ModulesEnum } from "../enums/ModulesEnum";
import { StatusEnum } from "../enums/StatusEnum";
export interface LevelsInterface {
    levels:Level[]
    moduleName:string;
    moduleId:ModulesEnum;
    isCompleted:boolean;
}
export interface Level{
    step:number;
    status:StatusEnum;
}