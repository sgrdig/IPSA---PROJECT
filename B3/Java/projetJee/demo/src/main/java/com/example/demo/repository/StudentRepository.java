package com.example.demo.repository;

import java.util.List;
import org.springframework.stereotype.Repository;

@Repository
public interface StudentRepository {
    // Repository for managing database operations

    public List<Student> findByName(String name);
}
