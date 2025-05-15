 **Module 4: Introduction to XSLT**, :

---

### **Module 4: Introduction to XSLT**

#### **4.1 What is XSLT?**

* **XSLT (eXtensible Stylesheet Language Transformations)** is a language designed for transforming XML documents into different formats such as XML, HTML, or plain text.
* It is **rule-based**, using templates to match and process XML nodes.
* Use cases:

  * Generating dynamic HTML pages from XML data
  * Transforming XML to another schema
  * Cleaning or restructuring XML before further processing

**Example:**

```xml
<xsl:template match="/product">
  <html><body>
    <h1><xsl:value-of select="name"/></h1>
  </body></html>
</xsl:template>
```

---

#### **4.2 XSLT Architecture: Input → XSLT → Output**

* XSLT operates as a **three-part system**:

  * **Input XML**: The data source.
  * **XSLT Stylesheet**: Contains transformation logic.
  * **Output**: Transformed document (XML, HTML, or text).

**Architecture Flow:**

```
[Input XML] + [XSLT Stylesheet] ──▶ [XSLT Processor] ──▶ [Output Document]
```

---

#### **4.3 Template Matching Model – `<xsl:template match>`**

* XSLT uses the concept of **template matching** to apply rules to selected XML elements.
* The processor looks for templates with matching **XPath expressions**.

**Syntax:**

```xml
<xsl:template match="/ecommerce/orders/order">
  <div>Order ID: <xsl:value-of select="@id"/></div>
</xsl:template>
```

* You can use `match="*"` for wildcard or `match="."` for the current node.

---

#### **4.4 Output Declaration – `<xsl:output method="xml|html" indent="yes">`**

* Defines how the output should be structured and formatted.
* Common attributes:

  * `method="xml"` or `method="html"` or `method="text"`
  * `indent="yes"` to improve readability
  * `encoding="UTF-8"` for character encoding

**Example:**

```xml
<xsl:output method="html" indent="yes" encoding="UTF-8"/>
```

---

#### **4.5 Tools: Browser View, Command-line, IDE (VSCode + Extensions)**

**✅ Browser View:**

* Modern browsers (like Chrome, Firefox) can apply XSLT stylesheets to XML if referenced with:

```xml
<?xml-stylesheet type="text/xsl" href="style.xsl"?>
```

**✅ Command-line:**

* Use **xsltproc**, **Saxon**, or **Xalan**:

```bash
xsltproc style.xsl data.xml > output.html
```

**✅ IDE Integration (VS Code):**

* Extensions:

  * `XSLT/XPath` by DeltaXML
  * `XML Tools`
  * `XML Viewer`
* Features:

  * Syntax highlighting
  * Auto-completion
  * Transformation preview

---

        ┌────────────┐           ┌───────────────┐
        │  Input XML │           │ XSLT Stylesheet│
        └────┬───────┘           └──────┬────────┘
             │                            │
             ▼                            ▼
          ┌─────────────────────────────────────┐
          │         XSLT Processor              │
          │  (e.g., browser engine, xsltproc,   │
          │   Saxon, Java transformer, etc.)    │
          └─────────────────────────────────────┘
                           │
                           ▼
         ┌────────────────────────────────┐
         │        Transformed Output      │
         │ (XML / HTML / Text / PDF etc.) │
         └────────────────────────────────┘

