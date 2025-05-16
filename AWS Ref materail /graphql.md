 **curated Angular + GraphQL Integration Learning Plan** using **free YouTube tutorials**, **official docs**, and **hands-on projects** — designed for beginners to intermediate developers looking to integrate GraphQL into Angular applications.

---

## 🧠 CURATED ANGULAR + GRAPHQL COURSE

**Duration**: 1 Week (2–3 hours/day)
**Level**: Beginner → Intermediate
**Goal**: Learn how to consume GraphQL APIs inside Angular apps using Apollo Client, write queries/mutations, and build full-stack GraphQL apps.

---

## 🗓️ DAY-WISE BREAKDOWN

---

### 🔹 **Day 1: Introduction to GraphQL and Angular Overview**

* 🎥 **YouTube**: [GraphQL Full Course (FreeCodeCamp)](https://www.youtube.com/watch?v=ed8SzALpx1Q) – (Watch first 45 mins)
* 📘 **Docs**: [GraphQL.org – Introduction](https://graphql.org/learn/)
* 🧠 Topics:

  * What is GraphQL?
  * Queries vs Mutations vs Subscriptions
  * REST vs GraphQL
* 🔍 Quick Angular Refresh:

  * Modules, Components, Services, HttpClient

---

### 🔹 **Day 2: Set Up Angular App + Install Apollo Client**

* 🎥 **YouTube**: [Angular + Apollo Setup (Traversy Media)](https://www.youtube.com/watch?v=ZQL7tL2S0oQ)
* 📘 **Docs**: [Apollo Angular Setup](https://www.apollographql.com/docs/angular/)
* 🛠️ Tasks:

  * `ng new angular-graphql-app`
  * Install:

    ```bash
    npm install apollo-angular apollo-angular-link-http apollo-client graphql-tag graphql
    ```
  * Configure `ApolloModule` in `AppModule`
* 💻 Lab:

  * Connect your Angular app to a public GraphQL API (e.g. [https://countries.trevorblades.com/](https://countries.trevorblades.com/))

---

### 🔹 **Day 3: Write Basic GraphQL Queries**

* 🎥 **YouTube**: [GraphQL Query in Angular](https://www.youtube.com/watch?v=IJq4Vh-J8xs)
* Topics:

  * How to use `gql` and `Apollo.query`
  * Handling responses and errors
* 💻 Lab:

  * Fetch countries, show them in a list with \*ngFor
  * Add loader and error messages

---

### 🔹 **Day 4: GraphQL Mutations in Angular**

* 🎥 **YouTube**: [Apollo Mutations in Angular](https://www.youtube.com/watch?v=e4XTn8Tvy80)
* Topics:

  * Writing mutations using `Apollo.mutate`
  * Sending variables to mutation
* 💻 Lab:

  * Create a simple form and submit data using mutation
  * Update frontend on mutation success

---

### 🔹 **Day 5: Advanced Features – Fragments, Variables, Caching**

* 📘 **Docs**: [Apollo Caching](https://www.apollographql.com/docs/react/caching/overview/)
* Topics:

  * GraphQL Fragments for reusability
  * Passing dynamic variables
  * Apollo Cache and Update strategy
* 💻 Lab:

  * Refactor queries using fragments
  * Apply optimistic UI update after mutation

---

### 🔹 **Day 6: Apollo Client with Subscriptions (Optional/Advanced)**

* 🎥 **YouTube**: [GraphQL Subscriptions Tutorial](https://www.youtube.com/watch?v=VjLdJ5J5g9w)
* Topics:

  * WebSocket setup for GraphQL Subscriptions
  * Using Apollo `subscribe`
* 💻 Lab:

  * Create a small example with subscription updates (e.g., chat, stock price)

---

### 🔹 **Day 7: Build a Full Project with Angular + GraphQL**

* 🎥 **YouTube**: [Angular + GraphQL Project](https://www.youtube.com/watch?v=2t1z3pJ7L4A)
* Project: **Book List Manager**

  * Fetch books with GraphQL Query
  * Add book with Mutation
  * Live update (optional subscription)
  * Styling with Angular Material

---

## 💼 BONUS RESOURCES

* 🔧 **GraphQL Playground for Testing APIs**:
  [https://countries.trevorblades.com/](https://countries.trevorblades.com/)
* 🚀 **Mock GraphQL APIs**:
  [https://mock.shop/graphql](https://mock.shop/graphql)
  [https://rickandmortyapi.com/graphql](https://rickandmortyapi.com/graphql)
* 🔍 **Apollo DevTools for Chrome**:
  [Apollo DevTools Extension](https://chromewebstore.google.com/detail/apollo-client-developer-t/jdkknkkbebbapilgoeccciglkfbmbnfm)

---

## 📦 FINAL OUTCOME

By the end of this course, you’ll be able to:

* Set up and configure Apollo in Angular
* Perform GraphQL queries and mutations
* Manage state and cache in Angular apps using Apollo
* Build real-world apps with full GraphQL support

---
