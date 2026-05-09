# 📘 Sorting Algorithms Empirical Analysis

This repository contains an empirical study of four fundamental sorting algorithms: **Selection Sort, Bubble Sort, Quick Sort, and Merge Sort**, implemented in Python as part of an Analysis of Algorithms course project.

---

## 📌 Project Overview

The goal of this project is to analyze and compare sorting algorithms based on:

- Execution time  
- Number of comparisons  
- Number of swaps  
- Behavior on different input types (sorted vs reverse-sorted)  
- Time complexity performance in real execution  

---

## ⚙️ Implemented Algorithms

The following algorithms are implemented from scratch:

- Selection Sort (O(n²))  
- Bubble Sort (O(n²))  
- Quick Sort (O(n log n) average case)  
- Merge Sort (O(n log n))  

No built-in sorting functions are used.

---

## 🧪 Experimental Setup

Each algorithm is tested on the following inputs:

- 5 elements (sorted)  
- 5 elements (reverse sorted)  
- 100 elements (sorted)  
- 100 elements (reverse sorted)  

### Measurements:
- Execution time using Python `time` module  
- Average of 3 runs for accuracy  
- Comparisons and swaps tracking  

---

## 📊 Key Findings

- Bubble Sort and Selection Sort perform poorly on large inputs due to **O(n²)** complexity  
- Quick Sort and Merge Sort perform efficiently due to **O(n log n)** complexity  
- Merge Sort shows the most consistent performance across all cases  
- Bubble Sort is most affected by reverse-sorted input  
- Selection Sort remains stable but inefficient  

---

## 📈 Conclusion

This project demonstrates how theoretical time complexities translate into real-world performance. Divide-and-conquer algorithms (Quick Sort and Merge Sort) significantly outperform quadratic algorithms for larger datasets.

---

## 🚀 Technologies Used

- Python 3  
- Time module  
- Basic array manipulation  

---

## 📂 How to Run

```bash
python sorting_analysis.py
