grep public_html/.htaccess -e RewriteRule | cut -d' ' -f2 | tr -d '[^$]' | grep -v '\.'
