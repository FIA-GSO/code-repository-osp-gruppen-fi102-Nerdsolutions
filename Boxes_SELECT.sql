SELECT BO.guid AS "BoxGUID",
BO.description AS "BoxDescription",
BO.category AS "BoxCategory",
BO.deployment_token AS "BoxDeployment",
BO.location AS "BoxLocation",
BO.location_home AS "BoxLocationHome",
BO.location_transport AS "BoxLocationTransport",
BO.location_deployment AS "BoxLocationDeployment",
BI.guid AS "BoxItemGUID",
BI.gtin AS "BoxItemGTIN",
BI.description AS "BoxItemDescription",
BI.quantity AS "BoxItemQuantity",
BI.unit AS "BoxItemUnit",
IC.guid AS "ItemContentGUID",
IC.gtin AS "ItemContentGTIN",
IC.description AS "ItemContenDescription",
IC.quantity AS "ItemContentQuantity",
IC.unit AS "ItemContentUnit",
IC.expiration_date AS "ItemContentExpirationDate"
FROM Boxes BO
LEFT JOIN BoxItems BI
ON BO.guid = BI.boxes_guid
LEFT JOIN ItemContents IC
ON BI.guid = IC.boxItems_guid;
