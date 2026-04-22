# SecurityContext

SecurityContext



# SecurityContext

A SecurityContext marks a location that has dangerous security implications, e.g. a DOM property like `innerHTML` that could cause Cross Site Scripting (XSS) security bugs when improperly handled.

## API

```
enum SecurityContext {
  NONE: SecurityContext.NONE;
  HTML: SecurityContext.HTML;
  STYLE: SecurityContext.STYLE;
  SCRIPT: SecurityContext.SCRIPT;
  URL: SecurityContext.URL;
  RESOURCE_URL: SecurityContext.RESOURCE_URL;
}
```

### NONE

### HTML

### STYLE

### SCRIPT

### URL

### RESOURCE\_URL

## Description

A SecurityContext marks a location that has dangerous security implications, e.g. a DOM property like `innerHTML` that could cause Cross Site Scripting (XSS) security bugs when improperly handled.

See DomSanitizer for more details on security in Angular applications.

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/api/core/SecurityContext>
