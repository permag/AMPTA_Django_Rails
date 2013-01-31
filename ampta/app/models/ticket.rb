class Ticket < ActiveRecord::Base
  attr_accessible :name, :description, :start_date, :end_date, :project_id, :status_id
  belongs_to :user
  belongs_to :project
  belongs_to :status
end
