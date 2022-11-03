from django.core.cache import cache

def get_tenants_map():
    return {"normal.manage.local": "normal", "root.manage.local": "root"}

def tenant_db_from_request(request):
    subdomain_prefix = request.COOKIES['Tenant']
    return subdomain_prefix if subdomain_prefix !="manage" else "default"
