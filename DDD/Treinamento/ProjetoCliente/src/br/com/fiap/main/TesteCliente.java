package br.com.fiap.main;

import br.com.fiap.beans.Carro;
import br.com.fiap.beans.Cliente;
import br.com.fiap.beans.Endereco;

public class TesteCliente {

	public static void main(String[] args) {
		
		// Instanciar Objetos
		
		Cliente objetoCliente = new Cliente();
		Endereco objetoEndereco = new Endereco();
		Carro objetoCarro = new Carro();
		
		// Entradas
		
		// Cliente
		
		objetoCliente.setNome("Joao");
		objetoCliente.setCpf("123.456.789-10");
		objetoCliente.setIdade(19);
		objetoCliente.setMensalidade(1800.00);
		objetoCliente.setEndereco(objetoEndereco);
		
		// Endereco
		
		objetoEndereco.setLogradouro("Av.Teste");
		objetoEndereco.setNumero(000);
		objetoEndereco.setComplemento("complemento de teste");
		objetoEndereco.setCep("000000-000");
		
		// Carro
		
		objetoCarro.setMarca("Honda");
		objetoCarro.setModelo("City");
		objetoCarro.setAno(2018);
		objetoCarro.setValor(122000.50);
		objetoCarro.setKm(1785.30);
		
		// Saidas
		
		System.out.println("Saidas do projeto: ");
		System.out.println(" ");
		
		System.out.println("Nome: " + objetoCliente.getNome() + 
				"\nIdade: " + objetoCliente.getIdade() + 
				"\nCPF: " + objetoCliente.getCpf() + 
				"\nMensalidade: " + objetoCliente.getMensalidade() + 
				"\nLogradouro: " + objetoEndereco.getLogradouro() +
				"\nNumero: " + objetoEndereco.getNumero() +
				"\nComplemento: " + objetoEndereco.getComplemento() + 
				"\nCEP: " + objetoEndereco.getCep() + 
				"\nMarca do carro: " + objetoCarro.getMarca() +
				"\nModelo: " + objetoCarro.getModelo() + 
				"\nAno: " + objetoCarro.getAno() + 
				"\nValor: " + objetoCarro.getValor());
		
	}

}
