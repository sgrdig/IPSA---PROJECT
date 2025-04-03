package com.example.demo.model;

import java.time.LocalDate;

public class Student {
    // Champs privés
    private int id;
    private String name;
    private String email;
    private int age;
    private LocalDate dob; // Date de naissance

    // Constructeur
    public Student(int id, String name, String email, int age, LocalDate dob) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.age = age;
        this.dob = dob; // Initialisation de la date de naissance
    }

    // Getters et setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public LocalDate getDob() {
        return dob;
    }

    public void setDob(LocalDate dob) {
        this.dob = dob;
    }

    // Méthode pour afficher les informations de l'étudiant
    public void displayStudentInfo() {
        System.out.println("Nom de l'étudiant: " + name);
        System.out.println("ID: " + id);
        System.out.println("Email: " + email);
        System.out.println("Age: " + age);
        System.out.println("Date de naissance: " + dob);
    }

}