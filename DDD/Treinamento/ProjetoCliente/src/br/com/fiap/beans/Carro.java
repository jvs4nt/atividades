package br.com.fiap.beans;

public class Carro {
	
	// Visibilidade, tipos e variaveis
	
	private String marca;
	private String modelo;
	private int ano;
	private double valor;
	private double km;
	
	// Setters (Entrada) e Getters (Exibir)
	
	public String getMarca() {
		return marca;
	}
	public void setMarca(String marca) {
		this.marca = marca;
	}
	public String getModelo() {
		return modelo;
	}
	public void setModelo(String modelo) {
		this.modelo = modelo;
	}
	public int getAno() {
		return ano;
	}
	public void setAno(int ano) {
		this.ano = ano;
	}
	public double getValor() {
		return valor;
	}
	public void setValor(double valor) {
		this.valor = valor;
	}
	public double getKm() {
		return km;
	}
	public void setKm(double km) {
		this.km = km;
	}

}
