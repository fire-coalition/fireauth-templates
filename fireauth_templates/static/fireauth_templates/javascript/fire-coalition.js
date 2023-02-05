$(document).ready(() => {
    'use strict';

    /**
     * Extend links to external website
     * » add target="_blank"
     * » add rel="noopener noreferer"
     */
    const externalLinks = () => {
        const internalHost = [location.hostname];
        const protocolPattern = /^https?:\/\//i;

        /**
         * Walk through all links on the current page
         */
        $('a').each((index, element) => {
            const href = $(element).attr('href');

            /**
             * Check if it's a http link
             */
            if (protocolPattern.test(href)) {
                const hrefHostname = $(new URL(href)).attr('hostname');

                if ($.inArray(hrefHostname, internalHost) === -1) {
                    $(element).attr('target', '_blank');
                    $(element).attr('rel', 'noopener noreferer');
                }
            }
        });
    };

    /**
     * Functions that need to be executed on successful ajax events
     */
    $(document).ajaxSuccess(() => {
        externalLinks();
    });

    /**
     * Functions that need to be executed on load
     */
    const init = () => {
        externalLinks();
    };

    /**
     * Start the show
     */
    init();
});
