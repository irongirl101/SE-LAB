### USE-CASE FLOW SPECIFICATION

Use Case: Request Package Delivery
Primary Actor: Sender Client
Supporting Actor: Delivery Rider

Preconditions
• Sender is authenticated and has provided a valid pickup and destination address.
• The platform can access rider availability and location data.
• The parcel is eligible for on-demand delivery.

Postconditions
• A delivery order is created and assigned to an eligible nearby rider, or the sender is informed that no rider is available.
• The sender can track delivery status and live rider location.
• Delivery completion requires destination OTP verification.

Main Success Scenario
1. Sender enters pickup address, destination address, parcel details, and delivery instructions.
2. Platform validates the request and identifies active riders within the configured service radius.
3. Platform ranks eligible riders by proximity and dispatches the request to the nearest rider.
4. Rider accepts the job and receives pickup, destination, and route details.
5. Platform optimizes the rider’s route, including any additional stops.
6. Rider picks up the parcel and updates the order status.
7. Sender receives status updates and live GPS telemetry while the parcel is in transit.
8. Rider reaches the destination and requests the recipient OTP.
9. Recipient provides the OTP; platform validates it successfully.
10. Rider completes the delivery, and the platform records completion and notifies the sender.

Alternate Flow: No Eligible Rider
At step 3, if no active rider is available within the configured radius, the platform marks the request as pending, notifies the sender, and retries dispatch when a suitable rider becomes available. If the sender cancels during the pending period, the platform closes the request without assigning a rider.

Business Rules
• Offline riders must never receive dispatches.
• A rider must explicitly accept before pickup details become active.
• Destination completion is blocked when the OTP is invalid or missing.