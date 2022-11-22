pragma solidity ^0.8.0;

contract Correo_contract {
    struct Correo_struct {
        string asunto;
        string body;
    }

    mapping(address => Correo_struct[]) correos;

    function enviarCorreo(string memory asunto, string memory body, address destinatario) public {
        Correo_struct[] storage correos_local = correos[destinatario];
        correos_local.push(Correo_struct(asunto, body));
    }

    function leerCorreo(address micorreo) public view returns (Correo_struct[] memory) {
        Correo_struct[] memory correos_local = correos[micorreo];
        return correos_local;
    }
}