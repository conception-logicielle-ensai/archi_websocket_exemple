kubectl delete -f backend/
kubectl delete -f frontend/
kubectl delete -f wsock/
kubectl apply -f backend/
kubectl apply -f frontend/
kubectl apply -f wsock/