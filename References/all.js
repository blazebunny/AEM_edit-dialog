/*
 *
 * ADOBE CONFIDENTIAL
 * __________________
 *
 *  Copyright 2017 Adobe Systems Incorporated
 *  All Rights Reserved.
 *
 * NOTICE:  All information contained herein is, and remains
 * the property of Adobe Systems Incorporated and its suppliers,
 * if any.  The intellectual and technical concepts contained
 * herein are proprietary to Adobe Systems Incorporated and its
 * suppliers and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material
 * is strictly forbidden unless prior written permission is obtained
 * from Adobe Systems Incorporated.
 */

(function($) {
    'use strict';

    var CHANNEL_ASSIGNMENT_TYPE_SELECTOR = '.screens-AssetSchedule-dates .coral-Form-field';

    /**
     * Validator for scheduled dates.
     */
    $(window).adaptTo('foundation-registry').register('foundation.validation.validator', {
        selector: CHANNEL_ASSIGNMENT_TYPE_SELECTOR,
        validate: function(el) {
            var $fields = $(CHANNEL_ASSIGNMENT_TYPE_SELECTOR);
            $fields.eq(0).attr('max', $fields.get(1).value);
            $fields.eq(1).attr('min', $fields.get(0).value);
        }
    });

}(window.Granite.$));
