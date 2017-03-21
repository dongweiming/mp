### source code start
from itertools import chain


class CheckRegistry:

    def __init__(self):
        self.registered_checks = []
        self.deployment_checks = []

    def register(self, check=None, *tags, **kwargs):
        kwargs.setdefault('deploy', False)

        def inner(check):
            check.tags = tags
            if kwargs['deploy']:
                if check not in self.deployment_checks:
                    self.deployment_checks.append(check)
            elif check not in self.registered_checks:
                self.registered_checks.append(check)
            return check

        if callable(check):
            return inner(check)
        else:
            if check:
                tags += (check, )
            return inner

    def tag_exists(self, tag, include_deployment_checks=False):
        return tag in self.tags_available(include_deployment_checks)

    def tags_available(self, deployment_checks=False):
        return set(chain(*[check.tags for check in self.get_checks(deployment_checks) if hasattr(check, 'tags')]))

    def get_checks(self, include_deployment_checks=False):
        checks = list(self.registered_checks)
        if include_deployment_checks:
            checks.extend(self.deployment_checks)
        return checks


registry = CheckRegistry()
register = registry.register
tag_exists = registry.tag_exists

### source code end
@register('mytag', 'another_tag')
def my_check(apps, **kwargs):
    pass


print tag_exists('another_tag')
print tag_exists('not_exists_tag')
