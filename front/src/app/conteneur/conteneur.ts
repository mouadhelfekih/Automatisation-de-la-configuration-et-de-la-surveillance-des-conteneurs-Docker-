
export class conteneur {
    Image:string;
    Names:string[];
    Id:string;
    Status:string;
    Ports:[{Type:string, PrivatePort:number, PublicPort:number, IP:string}];
    Created:string;
    Command:string;
    }
