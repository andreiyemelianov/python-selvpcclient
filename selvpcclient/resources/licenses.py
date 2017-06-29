from selvpcclient import base
from selvpcclient.util import resource_filter


class License(base.Resource):
    """Represents a license."""

    def delete(self):
        """Delete current license from domain."""
        self.manager.delete(self.id)


class LicenseManager(base.Manager):
    """Manager class for manipulating licenses."""
    resource_class = License

    @resource_filter
    def list(self, detailed=False):
        """Get list of all licenses in current domain.

        :param bool detailed: Include info about servers. (optional)
        :rtype: list of :class:`License`
        """
        return self._list('/licenses?detailed=' + str(detailed), 'licenses')

    def add(self, project_id, licenses):
        """Create licenses for project.

        :param string project_id: Project id.
        :param dict licenses: Dict with key `licenses` and value as array
                              of items region, quantity and type::

                                 {
                                     "licenses": [{
                                        "region": "ru-1",
                                        "quantity": 4,
                                        "type": "license_windows_2012_standard"
                                     },
                                     {
                                        "region": "ru-2",
                                        "quantity": 1,
                                        "type": "license_windows_2012_standard"
                                     }]
                                 }
        :rtype: list of :class:`License`
        """
        url = '/licenses/projects/{}'.format(project_id)
        return self._list(url, 'licenses', body=licenses)

    def show(self, license_id):
        """ Show detailed license information.

        :param string license_id: License id.
        :rtype: :class:`License`
        """
        return self._get('/licenses/{}'.format(license_id),
                         response_key='license')

    def delete(self, license_id):
        """Delete license from domain.

        :param string license_id: License id.
        """
        self._delete('/licenses/{}'.format(license_id))