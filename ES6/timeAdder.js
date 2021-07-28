function timeAdder(value1,label1,value2,label2){
    if(value1<=0 && value2<=0){
        return false;
    }else{
        var value3;
        var label3;
        var answer = [];
        switch(label1){
            case 'seconds':
                if(value1>1){
                    switch(label2){
                        case 'days':
                            if(value2>1){
                                value3 = value1+(value2*86400);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                        case 'day':
                            if(value2===1){
                                value3 = value1+(value2*86400);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hours':
                            if(value2>1){
                                value3 = value1+(value2*3600);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hour':
                            if(value2===1){
                                value3 = value1+(value2*3600);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minutes':
                            if(value2>1){
                                value3 = value1+(value2*60);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minute':
                            if(value2===1){
                                value3 = value1+(value2*60);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'seconds':
                            if(value2>1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'second':
                            if(value2===1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        
                        default:
                            return false;
                    }
                }else{
                    //The value1 must be > 1 because it's plural
                    return false;
                }
                break;
            case 'minutes':
                if(value1>1){
                    switch(label2){
                        case 'days':
                            if(value2>1){
                                value3 = value1+(value2*1440);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                        case 'day':
                            if(value2===1){
                                value3 = value1+(value2*1440);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hours':
                            if(value2>1){
                                value3 = value1+(value2*60);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hour':
                            if(value2===1){
                                value3 = value1+(value2*60);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minutes':
                            if(value2>1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minute':
                            if(value2===1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'seconds':
                            if(value2>1){
                                value3 = value2+(value1*60);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'second':
                            if(value2===1){
                                value3 = value2+(value1*60);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;                      
                        default:
                            return false;
                    }
                }else{
                    //The value1 must be > 1 because it's plural
                    return false;
                }
                break;
            case 'hours':
                if(value1>1){
                    switch(label2){
                        case 'days':
                            if(value2>1){
                                value3 = value1+(value2*24);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                        case 'day':
                            if(value2===1){
                                value3 = value1+(value2*24);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hours':
                            if(value2>1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hour':
                            if(value2===1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minutes':
                            if(value2>1){
                                value3 = value2+(value1*60);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minute':
                            if(valu2===1){
                                value3 = value2+(value1*60);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'seconds':
                            if(value2>1){
                                value3 = value2+(value1*3600);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'second':
                            if(value2===1){
                                value3 = value2+(value1*3600);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        
                        default:
                            return false;
                    }
                }else{
                    //The value1 must be > 1 because it's plural
                    return false;
                }
                break;
            case 'days':
                if(value1>1){
                    switch(label2){
                        case 'days':
                            if(value2>1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                        case 'day':
                            if(value2===1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hours':
                            if(value2>1){
                                value3 = value2+(value1*24);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hour':
                            if(value2===1){
                                value3 = value2+(value1*24);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minutes':
                            if(value2>1){
                                value3 = value2+(value1*1440);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minute':
                            if(value2===1){
                                value3 = value2+(value1*1440);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'seconds':
                            if(value2>1){
                                value3 = value2+(value1*86400);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'second':
                            if(value2===1){
                                value3 = value2+(value1*86400);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        
                        default:
                            return false;
                    }
                }else{
                    //The value1 must be > 1 because it's plural
                    return false;
                }
                break;
            

                

            case 'second':
                if(value1===1){
                    switch(label2){
                        case 'days':
                            if(value2>1){
                                value3 = value1+(value2*86400);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                        case 'day':
                            if(value2===1){
                                value3 = value1+(value2*86400);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hours':
                            if(value2>1){
                                value3 = value1+(value2*3600);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hour':
                            if(value2===1){
                                value3 = value1+(value2*3600);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minutes':
                            if(value2>1){
                                value3 = value1+(value2*60);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minute':
                            if(value2===1){
                                value3 = value1+(value2*60);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'seconds':
                            if(value2>1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'second':
                            if(value2===1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        
                        default:
                            return false;
                    }
                }else{
                    //The value1 must be === 1 because it's singular
                    return false;
                }
                break;
            case 'minute':
                if(value1===1){
                    switch(label2){
                        case 'days':
                            if(value2>1){
                                value3 = value1+(value2*1440);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                        case 'day':
                            if(value2===1){
                                value3 = value1+(value2*1440);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hours':
                            if(value2>1){
                                value3 = value1+(value2*60);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hour':
                            if(value2===1){
                                value3 = value1+(value2*60);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minutes':
                            if(value2>1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minute':
                            if(value2===1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'seconds':
                            if(value2>1){
                                value3 = value2+(value1*60);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'second':
                            if(value2===1){
                                value3 = value2+(value1*60);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        
                        default:
                            return false;
                    }
                }else{
                    //The value1 must be === 1 because it's singular
                    return false;
                }
                break;
            case 'hour':
                if(value1===1){
                    switch(label2){
                        case 'days':
                            if(value2>1){
                                value3 = value1+(value2*24);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                        case 'day':
                            if(value2===1){
                                value3 = value1+(value2*24);
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hours':
                            if(value2>1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hour':
                            if(value2===1){
                                value3 = value1+value2;
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minutes':
                            if(value2>1){
                                value3 = value2+(value1*60);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minute':
                            if(value2===1){
                                value3 = value2+(value1*60);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'seconds':
                            if(value2>1){
                                value3 = value2+(value1*3600);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'second':
                            if(value2===1){
                                value3 = value2+(value1*3600);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        
                        default:
                            return false;
                    }
                }else{
                    //The value1 must be === 1 because it's singular
                    return false;
                }
                break;
            case 'day':
                if(value1===1){
                    switch(label2){
                        case 'days':
                            if(value2>1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                        case 'day':
                            if(value2===1){
                                value3 = value1+value2;
                                label3 = label1;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hours':
                            if(value2>1){
                                value3 = value2+(value1*24);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'hour':
                            if(value2===1){
                                value3 = value2+(value1*24);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minutes':
                            if(value2>1){
                                value3 = value2+(value1*1440);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'minute':
                            if(value2===1){
                                value3 = value2+(value1*1440);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'seconds':
                            if(value2>1){
                                value3 = value2+(value1*86400);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        case 'second':
                            if(value2===1){
                                value3 = value2+(value1*86400);
                                label3 = label2;
                                answer.push(value3,label3)
                                return answer;
                            }else{
                                return false;
                            }
                            break;
                        
                        default:
                            return false;
                    }
                }else{
                    //The value1 must be === 1 because it's singular
                    return false;
                }
                break;
            
            default:
                return false;
        }
        
    }
 }
 
 console.log(timeAdder(5,'hour',3,'hours'));