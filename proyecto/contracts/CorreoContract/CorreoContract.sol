pragma solidity ^0.8.0;

contract Correo_contract {

    struct Correo_struct_Enviados {
        address remitente;
        string asunto;
        string body;
        string fecha;
        address destinatario;
    }
    struct Correo_struct_Recibidos {
        address remitente;
        string asunto;
        string body;
        string fecha;
        address destinatario;
    }

    mapping(address => Correo_struct_Enviados[]) correose;
    mapping(address => Correo_struct_Recibidos[]) correosr;

    
    function enviarCorreo(address remitente, string memory asunto, string memory body, string memory fecha, address destinatario) public {
        Correo_struct_Recibidos[] storage correos_local = correosr[destinatario];
        correos_local.push(Correo_struct_Recibidos(remitente, asunto, body, fecha, destinatario));
        Correo_struct_Enviados[] storage correos_locall = correose[remitente];
        correos_locall.push(Correo_struct_Enviados(remitente, asunto, body, fecha, destinatario));
    }

    function leerCorreosRecibidos(address micorreo) public view returns (Correo_struct_Recibidos[] memory){
        Correo_struct_Recibidos[] memory correos_local = correosr[micorreo];
        return correos_local;
    }


    function leerBandejaEntrada(address micorreo) public view returns (Correo_struct_Enviados[] memory){
        Correo_struct_Enviados[] memory correos_locall = correose[micorreo];
        return correos_locall;
    }

    function eliminarBandejaEntrada(address micorreo) public {
        require (keccak256(abi.encode(correose[micorreo])) != keccak256(abi.encode("")), "Error, this address is not registered yet");
        delete correose[micorreo];
    }

}