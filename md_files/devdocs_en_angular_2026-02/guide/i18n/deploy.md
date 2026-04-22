# Deploy multiple locales

Deploy multiple locales



# Deploy multiple locales

  

If `myapp` is the directory that contains the distributable files of your project, you typically make different versions available for different locales in locale directories. For example, your French version is located in the `myapp/fr` directory and the Spanish version is located in the `myapp/es` directory.

The HTML `base` tag with the `href` attribute specifies the base URI, or URL, for relative links. If you set the `"localize"` option in [`angular.json`](https://angular.dev/reference/configs/workspace-config "Angular workspace configuration | Angular") workspace build configuration file to `true` or to an array of locale IDs, the CLI adjusts the base `href` for each version of the application. To adjust the base `href` for each version of the application, the CLI adds the locale to the configured `"subPath"`. Specify the `"subPath"` for each locale in your [`angular.json`](https://angular.dev/reference/configs/workspace-config "Angular workspace configuration | Angular") workspace build configuration file. The following example displays `"subPath"` set to an empty string.

```
"projects": {
    "angular.io-example": {
      // ...
      "i18n": {
        "sourceLocale": "en-US",
        "locales": {
          "fr": {
            "translation": "src/locale/messages.fr.xlf",
            "subPath": ""
          }
        }
      },
      "architect": {
        // ...
      }
    }
  }
  // ...
}
```

## Configure a server

Typical deployment of multiple languages serve each language from a different subdirectory. Users are redirected to the preferred language defined in the browser using the `Accept-Language` HTTP header. If the user has not defined a preferred language, or if the preferred language is not available, then the server falls back to the default language. To change the language, change your current location to another subdirectory. The change of subdirectory often occurs using a menu implemented in the application.

For more information on how to deploy apps to a remote server, see [Deployment](https://angular.dev/tools/cli/deployment "Deployment | Angular").

**IMPORTANT:** If you are using [Server rendering](../ssr) with `outputMode` set to `server`, Angular automatically handles redirection dynamically based on the `Accept-Language` HTTP header. This simplifies deployment by eliminating the need for manual server or configuration adjustments.

### Nginx example

The following example displays an Nginx configuration.

```
http {
    # Browser preferred language detection (does NOT require
    # AcceptLanguageModule)
    map $http_accept_language $accept_language {
        ~*^de de;
        ~*^fr fr;
        ~*^en "";
    }
    # ...
}

server {
    listen 80;
    server_name localhost;
    root /www/data;

    # Fallback to default language if no preference defined by browser
    if ($accept_language ~ "^$") {
        set $accept_language "fr";
    }

    # Redirect "/" to Angular application in the preferred language of the browser
    rewrite ^/$ /$accept_language permanent;

    # Everything under the Angular application is always redirected to Angular in the
    # correct language
    location ~ ^/(fr|de|$) {
        if ($accept_language = "") {
            try_files $uri /index.html?$args;
        }
        try_files $uri /$1/index.html?$args;
    }
    # ...
}
```

### Apache example

The following example displays an Apache configuration.

```
# docregion
<VirtualHost *:80>
    ServerName localhost
    DocumentRoot /www/data

    <Directory "/www/data">
        # Enable rewrite engine for URL manipulation
        RewriteEngine on
        RewriteBase /

        # Serve 'index.html' for root-level access
        RewriteRule ^../index\.html$ - [L]

        # If the requested file or directory does not exist, redirect to 'index.html'
        RewriteCond %{REQUEST_FILENAME} !-f
        RewriteCond %{REQUEST_FILENAME} !-d
        RewriteRule (..) $1/index.html [L]

        # Language-based redirection based on HTTP Accept-Language header

        # Redirect German users to the '/de/' directory
        RewriteCond %{HTTP:Accept-Language} ^de [NC]
        RewriteRule ^$ /de/ [R]

        # Redirect English-speaking users to the '/en/' directory
        RewriteCond %{HTTP:Accept-Language} ^en [NC]
        RewriteRule ^$ /en/ [R]

        # Redirect users with unsupported languages (not 'en' or 'de') to the '/fr/' directory
        RewriteCond %{HTTP:Accept-Language} !^en [NC]
        RewriteCond %{HTTP:Accept-Language} !^de [NC]
        RewriteRule ^$ /fr/ [R]
    </Directory>
</VirtualHost>
```

Super-powered by Google ©2010–2025.  
Code licensed under an MIT-style License. Documentation licensed under CC BY 4.0.  
<https://angular.dev/guide/i18n/deploy>
